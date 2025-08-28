grammar Lista;

lista : '[' elementos? ']' ;
elementos : elemento (',' elemento)* ;
elemento : NUMBER | STRING ;

NUMBER : [0-9]+ ;
STRING : '"' (~["])* '"' ;
WS : [ \t\r\n]+ -> skip ;