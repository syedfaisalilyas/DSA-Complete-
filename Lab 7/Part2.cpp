#include <iostream>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

class Stack {
private:
    vector<int> items;

public:
    bool isEmpty() {
        return items.empty();
    }

    void push(int item) {
        items.push_back(item);
    }

    int pop() {
        if (!isEmpty()) {
            int item = items.back();
            items.pop_back();
            return item;
        } else {
            throw runtime_error("pop from empty stack");
        }
    }

    int peek() {
        if (!isEmpty()) {
            return items.back();
        } else {
            throw runtime_error("peek from empty stack");
        }
    }

    string toString() {
        stringstream ss;
        for (int item : items) {
            ss << item << " ";
        }
        return ss.str();
    }
};

void postfixCalculator(string expression) {
    Stack stack;
    stringstream ss(expression);
    string token;

    while (ss >> token) {
        if (isdigit(token[0]) || (token[0] == '-' && isdigit(token[1]))) {
            stack.push(stoi(token));
        } else if (token == "+") {
            int operand2 = stack.pop();
            int operand1 = stack.pop();
            stack.push(operand1 + operand2);
        } else if (token == "-") {
            int operand2 = stack.pop();
            int operand1 = stack.pop();
            stack.push(operand1 - operand2);
        } else if (token == "*") {
            int operand2 = stack.pop();
            int operand1 = stack.pop();
            stack.push(operand1 * operand2);
        } else if (token == "/") {
            int operand2 = stack.pop();
            int operand1 = stack.pop();
            stack.push(operand1 / operand2);
        } else if (token == "%") {
            int operand2 = stack.pop();
            int operand1 = stack.pop();
            stack.push(operand1 % operand2);
        } else if (token == "?") {
            cout << stack.toString() << endl;
        } else if (token == "^") {
            cout << stack.peek() << endl;
        } else if (token == "!") {
            stack.pop();
        }
    }
}

int main() {
    string postfixExpression = "5 3 4 + * 2 / ? ^";
    postfixCalculator(postfixExpression);

    return 0;
}
