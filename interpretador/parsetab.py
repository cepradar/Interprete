
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

<<<<<<< HEAD
_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEDIVIDE EQUAL ID MINUS NUMBER PLUS TIMESstatement : ID EQUAL expressionexpression : expression PLUS expression\n                      | expression MINUS expression\n                      | expression TIMES expression\n                      | expression DIVIDE expressionexpression : NUMBERexpression : ID'
    
_lr_action_items = {'ID':([0,3,7,8,9,10,],[2,4,4,4,4,4,]),'$end':([1,4,5,6,11,12,13,14,],[0,-7,-1,-6,-2,-3,-4,-5,]),'EQUAL':([2,],[3,]),'NUMBER':([3,7,8,9,10,],[6,6,6,6,6,]),'PLUS':([4,5,6,11,12,13,14,],[-7,7,-6,-2,-3,-4,-5,]),'MINUS':([4,5,6,11,12,13,14,],[-7,8,-6,-2,-3,-4,-5,]),'TIMES':([4,5,6,11,12,13,14,],[-7,9,-6,9,9,-4,-5,]),'DIVIDE':([4,5,6,11,12,13,14,],[-7,10,-6,10,10,-4,-5,]),}
=======
_lr_signature = "leftPLUSMINUSleftTIMESDIVIDErightTIMESCIN COMMA COUT DEQUAL DISTINT DIVIDE ELSE ENDL EQUAL FOR GREATER GREATEREQUAL ID IF INT LBLOCK LBRACKET LESS LESSEQUAL LPAREN MINUS MINUSMINUS NUMBER PLUS PLUSPLUS POINT QUOTES RBLOCK RBRACKET RPAREN SEMICOLON STRING TIMES WHILEstatement : INT ID EQUAL expression SEMICOLONstatement : COUT expression SEMICOLONexpression : expression PLUS expression\n                      | expression MINUS expression\n                      | expression TIMES expression\n                      | expression DIVIDE expressionexpression : '(' expression ')'expression : NUMBERexpression : ID"
    
_lr_action_items = {'INT':([0,],[2,]),'COUT':([0,],[3,]),'$end':([1,10,22,],[0,-2,-1,]),'ID':([2,3,6,9,11,12,13,14,],[4,8,8,8,8,8,8,8,]),'(':([3,6,9,11,12,13,14,],[6,6,6,6,6,6,6,]),'NUMBER':([3,6,9,11,12,13,14,],[7,7,7,7,7,7,7,]),'EQUAL':([4,],[9,]),'SEMICOLON':([5,7,8,16,17,18,19,20,21,],[10,-8,-9,22,-3,-4,-5,-6,-7,]),'PLUS':([5,7,8,15,16,17,18,19,20,21,],[11,-8,-9,11,11,-3,-4,-5,-6,-7,]),'MINUS':([5,7,8,15,16,17,18,19,20,21,],[12,-8,-9,12,12,-3,-4,-5,-6,-7,]),'TIMES':([5,7,8,15,16,17,18,19,20,21,],[13,-8,-9,13,13,13,13,-5,-6,-7,]),'DIVIDE':([5,7,8,15,16,17,18,19,20,21,],[14,-8,-9,14,14,14,14,-5,-6,-7,]),')':([7,8,15,17,18,19,20,21,],[-8,-9,21,-3,-4,-5,-6,-7,]),}
>>>>>>> 0f83a4ac23ef087bbf132e83be0c938e1da6d462

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

<<<<<<< HEAD
_lr_goto_items = {'statement':([0,],[1,]),'expression':([3,7,8,9,10,],[5,11,12,13,14,]),}
=======
_lr_goto_items = {'statement':([0,],[1,]),'expression':([3,6,9,11,12,13,14,],[5,15,16,17,18,19,20,]),}
>>>>>>> 0f83a4ac23ef087bbf132e83be0c938e1da6d462

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
<<<<<<< HEAD
  ('statement -> ID EQUAL expression','statement',3,'p_statement_assign','parser.py',18),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',22),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',23),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',24),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',25),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',36),
  ('expression -> ID','expression',1,'p_expression_name','parser.py',40),
=======
  ('statement -> INT ID EQUAL expression SEMICOLON','statement',5,'p_statement_assign','parser.py',19),
  ('statement -> COUT expression SEMICOLON','statement',3,'p_statement_expr','parser.py',23),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',27),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',28),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',29),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',30),
  ('expression -> ( expression )','expression',3,'p_expression_group','parser.py',45),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',49),
  ('expression -> ID','expression',1,'p_expression_id','parser.py',53),
>>>>>>> 0f83a4ac23ef087bbf132e83be0c938e1da6d462
]