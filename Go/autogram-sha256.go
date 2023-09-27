package main

import "fmt"
import "crypto/sha256"

func main(){

	numbers_dict := map[string]string{
		"zero":"0",
		"one":"1",
		"two":"2",
		"three":"3",
		"four":"4",
		"five":"5",
		"six":"6",
		"seven":"7",
		"eight":"8",
		"nine":"9" }

	alphabets := []string{"a","b","c","d","e","f"}
    numbers_words := []string{"zero","one","two","three","four","five","six","seven","eight","nine"}

	for _, a1 := range alphabets {
		for _, a2 := range alphabets {
			for _, n1 := range numbers_words {
				for _, n2 := range numbers_words {
					for _, n3 := range numbers_words {
						for _, n4 := range numbers_words {
							for _, n5 := range numbers_words {

								autogram := numbers_dict[n1] + numbers_dict[n2] + numbers_dict[n3] + a1 + numbers_dict[n4] + a2 + numbers_dict[n5]

								sentence := fmt.Sprintf("The SHA256 for this sentence begins with: %s, %s, %s, %s, %s, %s and %s.", n1, n2, n3, a1, n4, a2, n5)

								sentence_byte := []byte(sentence)

								hasher := sha256.New()

								hasher.Write(sentence_byte)

								hashBytes := hasher.Sum(nil)

								sentence_hash := fmt.Sprintf("%x", hashBytes)

								if autogram == sentence_hash[:7] {
                                    fmt.Println(sentence)
                                    fmt.Println(sentence_hash)
								}
								
							}
						}
					}
				}
			}
		}
	}
}
