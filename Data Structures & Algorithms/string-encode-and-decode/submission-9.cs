public class Solution {
    /*
        Encode:
        4#chat5#hello

        ['chat', 'hello']
    */

    private char delimiter = '#';

    public string Encode(IList<string> strs) {
        var res = new StringBuilder();

        foreach (var str in strs) {
            res.Append(str.Length);
            res.Append(this.delimiter);
            res.Append(str);
        }

        return res.ToString();
    }

    public List<string> Decode(string s) {
        var res = new List<string>();

        var i = 0;

        while (i < s.Length) {
            var currentCount = new StringBuilder();

            while (Char.IsDigit(s[i])) {
                currentCount.Append(s[i]);
                i++;
            }

            if (s[i] == this.delimiter) {
                i++;
            } else {
                // throw exception
            }

            var wordLength = Int32.Parse(currentCount.ToString());

            var currentString = s.Substring(i, wordLength);

            res.Add(currentString);
            i += wordLength;
        }

        return res;
   }
}
