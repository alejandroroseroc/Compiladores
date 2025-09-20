# semantic_analyzer/SemanticVisitor.py
from generated.WhileLangVisitor import WhileLangVisitor
from generated.WhileLangParser import WhileLangParser
from .SymbolTable import SymbolTable, Symbol

class SemanticVisitor(WhileLangVisitor):
    def __init__(self):
        self.table = SymbolTable()

    # ===== declaraciones, asignaciones, bloques =====

    def visitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()  # 'int' | 'string'
        self.table.insert(var_name, Symbol(var_name, type_name))

        # inicialización opcional
        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if expr_type != 'error_type' and expr_type is not None and expr_type != type_name:
                print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{type_name}'.")
        return None

    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)
        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' a la que se intenta asignar no ha sido declarada.")
            return None

        expr_type = self.visit(ctx.expr())
        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{symbol.type}'.")
        return None

    def visitBlock(self, ctx:WhileLangParser.BlockContext):
        self.table.enter_scope()
        for st in ctx.statement():
            self.visit(st)
        self.table.exit_scope()
        return None

    # ===== if / while =====

    def visitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        # condición (debe resultar "booleana"; la tratamos como 'int')
        _cond_t = self.visit(ctx.expr())
        # bloque THEN
        self.visit(ctx.block(0))
        # bloque ELSE (opcional)
        if ctx.block(1):
            self.visit(ctx.block(1))
        return None

    def visitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        _cond_t = self.visit(ctx.expr())
        self.visit(ctx.block())
        return None

    def visitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        return None

    def visitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        return None

    # ===== expresiones (etiquetadas) =====

    def visitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        name = ctx.ID().getText()
        sym = self.table.lookup(name)
        if sym is None:
            print(f"Error Semántico: La variable '{name}' no ha sido declarada.")
            return 'error_type'
        return sym.type

    def visitNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        return 'int'

    def visitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        return 'string'

    def visitParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        lt = self.visit(ctx.expr(0))
        rt = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if lt == 'error_type' or rt == 'error_type':
            return 'error_type'

        # Concatenación de strings con '+'
        if op == '+' and lt == 'string' and rt == 'string':
            return 'string'

        # Aritmética: solo int con int
        if lt == 'int' and rt == 'int':
            return 'int'

        print(f"Error Semántico: Operación aritmética inválida entre '{lt}' {op} '{rt}'.")
        return 'error_type'

    def visitComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        lt = self.visit(ctx.expr(0))
        rt = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if lt == 'error_type' or rt == 'error_type':
            return 'error_type'

        # int comparado con int: permitido con todos los operadores
        if lt == 'int' and rt == 'int':
            return 'int'  # tratamos booleano como int

        # string comparado con string: solo == y !=
        if lt == 'string' and rt == 'string':
            if op in ('==', '!='):
                return 'int'
            print(f"Error Semántico: Comparación de strings inválida con operador '{op}'.")
            return 'error_type'

        print(f"Error Semántico: Comparación entre tipos incompatibles ({lt} vs {rt}).")
        return 'error_type'
