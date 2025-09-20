# semantic_analyzer/SemanticVisitor.py
from generated.IfElseLangVisitor import IfElseLangVisitor
from generated.IfElseLangParser import IfElseLangParser
from .SymbolTable import SymbolTable, Symbol

class SemanticVisitor(IfElseLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        # NUEVO: rastrear la función actual y validar 'return'
        self.current_function = None

    # ========= declaraciones / asignaciones / bloques =========

    def visitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()
        symbol = Symbol(name=var_name, type=type_name, category='variable')
        self.table.insert(var_name, symbol)

        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
                print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a la variable '{var_name}' de tipo '{symbol.type}' en su declaración.")
        return None

    def visitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return None
        
        if symbol.category == 'function':
            print(f"Error Semántico: No se puede asignar un valor a la función '{var_name}'.")
            return None

        expr_type = self.visit(ctx.expr())
        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a la variable '{var_name}' de tipo '{symbol.type}'.")
        return None

    # ========= funciones =========

    def visitFunctionDecl(self, ctx:IfElseLangParser.FunctionDeclContext):
        func_name = ctx.ID().getText()
        return_type = ctx.type_().getText()
        
        # 1) parámetros
        param_symbols = []
        if ctx.paramList():
            for param_ctx in ctx.paramList().param():
                param_name = param_ctx.ID().getText()
                param_type = param_ctx.type_().getText()
                param_symbols.append(Symbol(name=param_name, type=param_type, category='variable'))

        # 2) símbolo función
        func_symbol = Symbol(name=func_name, type=return_type, category='function', params=param_symbols)

        # 3) registrar función en ámbito actual (global normalmente)
        self.table.insert(func_name, func_symbol)

        # 4) set current_function
        self.current_function = func_symbol

        # 5) ámbito propio de la función
        self.table.enter_scope()

        # 6) parámetros como variables locales
        for p in param_symbols:
            self.table.insert(p.name, p)

        # 7) visitar bloque
        self.visitChildren(ctx.block())

        # 8) salir del ámbito
        self.table.exit_scope()

        # 9) limpiar current_function
        self.current_function = None
        return None

    # llamada a función como expresión
    def visitFuncCallExpr(self, ctx:IfElseLangParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        symbol = self.table.lookup(func_name)

        if symbol is None:
            print(f"Error Semántico: La función '{func_name}' no ha sido declarada.")
            return 'error_type'
        
        if symbol.category != 'function':
            print(f"Error Semántico: El identificador '{func_name}' no es una función, no se puede llamar.")
            return 'error_type'
        
        provided_args = ctx.argList().expr() if ctx.argList() else []
        expected_params = symbol.params

        if len(provided_args) != len(expected_params):
            print(f"Error Semántico: La función '{func_name}' esperaba {len(expected_params)} argumentos, pero recibió {len(provided_args)}.")
            return 'error_type'
        
        for i, arg_expr in enumerate(provided_args):
            arg_type = self.visit(arg_expr)
            param_type = expected_params[i].type
            if arg_type != param_type:
                print(f"Error Semántico: En la llamada a '{func_name}', el argumento {i+1} es de tipo '{arg_type}', pero se esperaba '{param_type}'.")
                return 'error_type'

        return symbol.type  # tipo de la expresión es el tipo de retorno

    # sentencia return
    def visitReturnStatement(self, ctx:IfElseLangParser.ReturnStatementContext):
        if self.current_function is None:
            print("Error Semántico: La sentencia 'return' solo puede aparecer dentro de una función.")
            return None
        
        return_type = self.visit(ctx.expr())
        expected_type = self.current_function.type

        if return_type != expected_type:
            print(f"Error Semántico: La función '{self.current_function.name}' debe retornar un valor de tipo '{expected_type}', pero se encontró '{return_type}'.")
        return None

    # ========= if / condition =========

    def visitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        self.visit(ctx.condition())

        # then
        self.table.enter_scope()
        for st in ctx.statement()[:len(ctx.statement()) // (2 if ctx.ELSE() else 1)]:
            self.visit(st)
        self.table.exit_scope()

        # else
        if ctx.ELSE():
            self.table.enter_scope()
            for st in ctx.statement()[len(ctx.statement()) // 2:]:
                self.visit(st)
            self.table.exit_scope()

        return None

    # ========= expresiones (etiquetadas) =========

    def visitIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        name = ctx.ID().getText()
        sym = self.table.lookup(name)
        if sym is None:
            print(f"Error Semántico: La variable '{name}' no ha sido declarada.")
            return 'error_type'
        if sym.category == 'function':
            print(f"Error Semántico: No se puede usar la función '{name}' como una variable en una expresión.")
            return 'error_type'
        return sym.type

    def visitNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        return 'int'

    def visitStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        return 'string'

    def visitParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitArithmeticExpr(self, ctx:IfElseLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()  # '+', '-', '*', '/'

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        # int (op) int -> int
        if left_type == 'int' and right_type == 'int':
            return 'int'

        # string + string -> string (solo concatenación con '+')
        if op == '+' and left_type == 'string' and right_type == 'string':
            return 'string'

        print(f"Error Semántico: El operador '{op}' no se puede aplicar a los tipos '{left_type}' y '{right_type}'.")
        return 'error_type'

    def visitComparisonExpr(self, ctx:IfElseLangParser.ComparisonExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        if left_type != right_type:
            print(f"Error Semántico: Comparación entre tipos incompatibles ({left_type} vs {right_type}).")
            return 'error_type'
        # tratamos 'booleano' como 'int' para este ejercicio
        return 'int'
