#pragma once
#include "ExprAst.h"



class VariableExprAST: public eEprAST {
    std::string name;
public:
    explicit VariableExprAST(std::string name): name(std::move(name)) {}
};
