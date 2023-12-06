#pragma once

class Response {
    std::unique_ptr<ExprAST> expr;
    int token;
public:
        Response(std::unique_ptr<ExprAST> expr, int token)
            : expr(std::move(expr)), token(token) {}

        std::unique_ptr<ExprAST> getExpr() {
            return std::move(expr);
        }

        int getToken() {
            return token;
        }
};

