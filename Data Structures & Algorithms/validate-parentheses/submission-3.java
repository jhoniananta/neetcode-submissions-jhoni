class Solution {
    public boolean isValid(String s) {
        Stack<Character> charStack = new Stack<>();

        for (int i =0; i<s.length(); i++){
           if(s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '['){
            charStack.push(s.charAt(i));
           } else {
            if(!charStack.isEmpty()){
                char temp = charStack.peek();
                if((s.charAt(i) == ')' && temp == '(') || (s.charAt(i) == '}' && temp == '{') || (s.charAt(i) == ']' && temp == '[')){
                    charStack.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
           }
        }
        if(charStack.isEmpty()){
            return true;
        } else {
            return false;
        }
    }
}
