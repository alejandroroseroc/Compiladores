grammar WhileLang;

program: statement+ EOF;

declaration: type ID (ASSIGN expr)? SEMI;

type: 'int' | 'string';

statement
    : assignment
    | ifStatement
    | whileStatement
    | declaration
    | breakStatement
    | continueStatement
    | block
    ;

condition
    : expr                       
    | expr (GT | LT | EQ | NE) expr  
    ;

block: LBRACE statement* RBRACE;

assignment: ID ASSIGN expr SEMI;

ifStatement
    : IF LPAREN expr RPAREN block
      (ELSE block)?
    ;

// TIP 6: el parser acepta 'a < b' (dos strings) sin error sintáctico.
// El error debe ser SEMÁNTICO (se maneja en SemanticVisitor.visitComparisonExpr).
whileStatement
    : WHILE LPAREN expr RPAREN block
    ;

breakStatement: BREAK SEMI;
continueStatement: CONTINUE SEMI;

// ======================
// Expresiones con etiquetas
// ======================
expr
    : ID                                       # idExpr
    | NUMBER                                   # numberExpr
    | STRING                                   # stringExpr
    | expr (LT | GT | GE | LE | EQ | NE) expr  # comparisonExpr
    | expr (PLUS | MINUS | MUL | DIV) expr     # arithmeticExpr
    | LPAREN expr RPAREN                       # parenExpr
    ;

// ======================
// Tokens
// ======================
IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';

LT: '<';
GT: '>';
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';

COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;
