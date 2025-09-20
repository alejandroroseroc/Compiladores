grammar IfElseLang;

program: (statement | functionDecl)+ EOF;

declaration: type ID ('=' expr)? SEMI; 

type: 'int' | 'string';

statement
    : assignment
    | ifStatement
    | declaration
    | returnStatement
    | expr SEMI
    ;

returnStatement: 'return' expr SEMI;

functionDecl: type ID LPAREN paramList? RPAREN block;
param: type ID;
paramList: param (',' param)*;

assignment: ID ASSIGN expr SEMI;

ifStatement
    : IF LPAREN condition RPAREN LBRACE statement* RBRACE
      (ELSE LBRACE statement* RBRACE)?
    ;

condition: expr; // condición es cualquier expresión "booleana" para este ejercicio

// ======================
// Expresiones con etiquetas (TODAS etiquetadas)
// ======================
expr
    : ID LPAREN argList? RPAREN               # funcCallExpr
    | ID                                      # idExpr
    | NUMBER                                  # numberExpr
    | STRING                                  # stringExpr
    | expr (LT | GT | GE | LE | EQ | NE) expr # comparisonExpr
    | expr (PLUS | MINUS | MUL | DIV) expr    # arithmeticExpr
    | LPAREN expr RPAREN                      # parenExpr
    | block                                   # blockExpr
    ;

argList: expr (',' expr)*;
block: LBRACE statement* RBRACE;

// ======================
// Tokens (poner los de 2 chars antes que los de 1 char)
// ======================
IF: 'if';
ELSE: 'else';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';

// Operadores de 2 caracteres primero
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';

GT: '>';
LT: '<';
ASSIGN: '=';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

// Soporta comillas dobles simples; puedes ampliar escapes si quieres
STRING: '"' (~["\r\n])* '"';

COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;
