class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        if(tokens.length == 0) return 0;

        for (String token : tokens){
            if( token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")){
                int val1 = stack.pop();
                int val2 = stack.pop();

                if(token.equals("+")){
                    stack.push(val2 + val1);
                } else if (token.equals("-")) {
                    stack.push(val2 - val1);
                } else if (token.equals("*")){
                    stack.push(val2 * val1);
                } else {
                    stack.push(val2 / val1);
                }

            } else {
                int val = Integer.parseInt(token);
                stack.push(val);
            }
        }

        return stack.pop();
    }
}
