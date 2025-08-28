grammar Asignaciones;

programa : asignacion+ ;
asignacion : ID '=' expresion ';' ;

expresion : expresion '+' expresion
          | expresion '*' expresion  
          | ID
          | NUMBER
          | '(' expresion ')'
          ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;