grammar Condicionales;

programa : sentencia+ ;

sentencia : asignacion
          | condicional
          ;

asignacion : ID '=' expresion ';' ;

condicional : 'if' '(' condicion ')' '{' sentencia+ '}' ;

condicion : expresion operadorComp expresion ;

operadorComp : '==' | '!=' | '<' | '>' | '<=' | '>=' ;

expresion : expresion '+' expresion
          | expresion '*' expresion
          | ID  
          | NUMBER
          | '(' expresion ')'
          ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;