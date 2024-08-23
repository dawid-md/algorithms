function isAlt(word) {
    let vowels = ['a', 'e', 'i', 'o', 'u']
    for(j=1; j<word.length; j++){
      if((vowels.includes(word[j]) && vowels.includes(word[j-1])) || (!vowels.includes(word[j]) && !vowels.includes(word[j-1]))){
        return false
      }
    }
    return true
  }

console.log(isAlt("amazon"))