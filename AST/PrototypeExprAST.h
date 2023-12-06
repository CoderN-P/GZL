#pragma once

class PrototypeExprAST {
    std::string name;
    std::vector<std::string> args;

public:
    PrototypeExprAST(std::string name, std::vector<std::string> args)
        : name(std::move(name)), args(std::move(args)) {}
};
