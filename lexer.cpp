#include <iostream>
#include <lexer.h>

static int lexer::getToken(){
    static int lastChar = ' ';

    while (lastChar == ' '){
        lastChar = getc(stdin)
    }

    if (isalpha(lastChar)){
        identifierStr = lastChar;

        while (isalnum(lastChar)){
            lastChar = getc(stdin);
            identifierStr += lastChar;
        }

        if (identifierStr == "be"){
            return tok_be;
        } else if (identifierStr == "smol"){
            return tok_smol;
        }

        return tok_identifier;
    }

    if (isdigit(lastChar) || lastChar == '.'){
        std::string numString;
        do {
            numString += lastChar;
            lastChar = getc(stdin);
        } while (isdigit(lastChar) || lastChar == '.');

        numVal = strtod(numString.c_str());
        return tok_number
    }

    if (lastChar == '|'){
        do {
            lastChar = getc(stdin);
        } while (lastChar != EOF && lastChar != '\n' && lastChar != '\r');

        if (lastChar != EOF){
            return getToken();
        }
    }

    if (lastChar == EOF){
        return tok_eof;
    }

    int curChar = lastChar;

    lastChar = getc(stdin);

    return curChar;
}

