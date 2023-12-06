#include "./AST/ExprAST.h"
#include "./lexer.h"
#include "./utils/Response.h"


Response ParseNumberExpr() {
    auto result = std::make_unique<NumberExprAST>(NumVal);
    int token = lexer::getToken();
    Response response = Response(std::move(result), token);
    return response;
}
