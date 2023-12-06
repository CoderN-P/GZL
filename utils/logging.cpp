#include "AST/ExprAST.h"

std::unique_pointer<ExprAST> LogError(const char *str) {
    fprintf(stderr, "LogError: %s\n", str);
    return nullptr;
}

std::unique_pointer<PrototypeExprAST> LogErrorP(const char *str) {
    LogError(str);
    return nullptr;
}
