grammar Calculadora;

prog: expresion EOF ;

// Reglas con precedencia
expresion
    : expresion '^' expresion          # Potencia         // mayor precedencia
    | expresion ('*'|'/') expresion    # MultDiv
    | expresion ('+'|'-') expresion    # AddSub  
    | '-' expresion                    # Negativo         // números negativos
    | funcion                          # Funciones
    | '(' expresion ')'                # Parentesis
    | NUMBER                           # Numero
    ;

funcion
    : 'sqrt' '(' expresion ')'         # FuncionSqrt
    | 'abs' '(' expresion ')'          # FuncionAbs
    ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;
