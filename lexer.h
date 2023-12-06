#pragma once

class lexer {
    enum Token {
        tok_eof = -1,

        tok_be = -2,
        tok_smol = -3,

        tok_identifier = -4,
        tok_number = -5,
    };

    static double numVal;
    static std::string identifierStr;
    static int getToken();

};
