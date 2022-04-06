<h2 align="center">.aboutMe()</h2>

```js
import me from "vietnam";
import now from "russia";

function getBio() {
    return {
        "Full name":    "Le Dinh Cuong",
        "Nationality":  me.nationality,
        "Quick bio":   "La vie est faite de petits bonheurs."
        "Description":  [
            "I'm originally from Thanh Hoa, Vietnam and an alumnus of [Lam Son High School for the Gifted]",
            "and [Academy of Cryptography Techniques]. Currenly, I'm an international student in Russia.",
            "I love the internet, technology, music, sports, dogs, cats, children, ... and building beautiful things."
        ],
        "Major":        "Software Engineering",
        "Experience":   "Web Developer, Designer, Photographer, Editor",
        "Address":      now.address,
        "Email":        "mail@ledinhcuong.com",
        "Website":     "https://ledinhcuong.com"
    }
}

function main() {
  let bio = getBio();
  for(let key in bio){
       let info = bio[key];
       console.info(key + ":\n\t=> " + info + "\n\n");
  } 
}

main()
```
