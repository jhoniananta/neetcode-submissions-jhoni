class Solution {

    public String encode(List<String> strs) {
        String encodedWords = "";
        for (String item : strs) {
            String count = Integer.toString(item.length());

            encodedWords += count.toString() + "#" + item;
        }

        return encodedWords;
    }

    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;

        while (i < s.length()) {
            int j = i;
            while (j < s.length() && s.charAt(j) != '#') {
                j++;
            }
            int len = Integer.parseInt(s.substring(i, j));

            int start = j + 1;
            int end = start + len;
            res.add(s.substring(start, end));

            i = end;
        }
        return res;
    }
}
