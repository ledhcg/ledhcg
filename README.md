<h2 align="center">.aboutMe()</h2>

```javascript
import nationality from "vietnam";
import now from "russia";

function getBio() {
	return {
        "Full name":    "Le Dinh Cuong",
        "Nationality"   nationality,
		"Quick bio:":   "A kind of metalHead-synthWave-cyberPunk-melomaniac-gearAddict-amateurMusician-traveler-foodLover-gamer-coder-programmer-catLover-sportsAficionado hybrid",
		"Description":  "I'm originally from Thanh Hoa, Vietnam and an alumnus of [Lam Son High School for the      Gifted] and [Academy of Cryptography Techniques]. Currenly, I'm an international student in Russia. I love the internet, technology, music, sports, dogs, cats, children, ... and building beautiful things.",
		"Major":        "Software Engineering"
        "Experience":   "FS Developer, Designer, Photographer, Editor"
		"Address":      now.address,
		"Email":        "mail@ledinhcuong.com",
		"Website:":     "https://ledinhcuong.com",
	}
}

function main() {
  let bio = getBio();
  for(let key in bio){
       let info = bio[key];
       console.info(info);
  } 
}

main()
```
