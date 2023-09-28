using System.Security.Cryptography;
using System.Text;

public class Autogram_SHA256{
    
    public static void Autogram_SHA256SUM(){

        Dictionary<string, string> numbers_dict = new Dictionary<string, string>{
            {"zero", "0"},
            {"one", "1"},
            {"two", "2"},
            {"three", "3"},
            {"four", "4"},
            {"five", "5"},
            {"six", "6"},
            {"seven", "7"},
            {"eight", "8"},
            {"nine", "9"}
        };

        string[] alphabets = {"a","b","c","d","e","f"};
        string[] numbers_words = {"zero","one","two","three","four","five","six","seven","eight","nine"};

        foreach (string a1 in alphabets) {
            foreach (string a2 in alphabets) {
                foreach (string n1 in numbers_words) {
                    foreach (string n2 in numbers_words) {
                        foreach (string n3 in numbers_words) {
                            foreach (string n4 in numbers_words) {
                                foreach (string n5 in numbers_words) {

                                    string autogram = numbers_dict[n1] + numbers_dict[n2] + numbers_dict[n3] + a1 + numbers_dict[n4] + a2 + numbers_dict[n5];

                                    string sentence = $"The SHA256 for this sentence begins with: {n1}, {n2}, {n3}, {a1}, {n4}, {a2} and {n5}.";

                                    // Convert the string to bytes (UTF-8 encoding is used here)
                                    byte[] sentence_byte = Encoding.UTF8.GetBytes(sentence);

                                    // Create an instance of the SHA-256 algorithm
                                    using SHA256 sha256 = SHA256.Create();

                                    // Compute the hash
                                    byte[] hashBytes = sha256.ComputeHash(sentence_byte);

                                    // Get the hexadecimal representation of the hash
                                    string sentence_hash = BitConverter.ToString(hashBytes).Replace("-", "").ToLower();

                                    if (autogram == sentence_hash.Substring(0, 7)){
                                        Console.WriteLine(sentence);
                                        Console.WriteLine(sentence_hash);
                                    }

                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
