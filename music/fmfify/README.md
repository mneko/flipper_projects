# fmfify.py

this guy converts RTTTL formatted files into the Flipper Music File format.


## how to use

- find your rttl file (it looks something like this 
```a song title:d=8,o=4,b=320,l=15:c#,32p,4e,32p,g#,32p,c#5,4p.,c5,4p.,1b.,4p.,b,32p,4a,32p,b,32p,a,p.,1g#.,2p,g#,32p,4a,32p,b,32p,a,4p.,g#,4p.,e,p.,e,32p,f#,4p.,4g,32p,1g#.,p.,c#,32p,4e,32p,g#,32p,c#5,4p.,c5,4p.,1b.,4p.,b,32p,4a,32p,b,32p,a,p.,1g#.,2p,g#,32p,4a,32p,b,32p,a,4p.,g#,4p.,e,p.,e,32p,f#,4p.,4g,32p,1g#.``` ) and is usually shared in plaintext

- rename the file extension to .fmf 

- drop the file in the same directory as fmfify.py

- run ```python fmfify.py```

- double check to make sure the file now looks like this 
```
Filetype: Flipper Music Format  
Version: 0  
BPM: 320  
Duration: 8  
Octave: 4  
Notes:c#,32p,4e,32p,g#,32p,c#5,4p.,c5,4p.,1b.,4p.,b,32p,4a,32p,b,32p,a,p.,1g#.,2p,g#,32p,4a,32p,b,32p,a,4p.,g#,4p.,e,p.,e,32p,f#,4p.,4g,32p,1g#.,p.,c#,32p,4e,32p,g#,32p,c#5,4p.,c5,4p.,1b.,4p.,b,32p,4a,32p,b,32p,a,p.,1g#.,2p,g#,32p,4a,32p,b,32p,a,4p.,g#,4p.,e,p.,e,32p,f#,4p.,4g,32p,1g#.
```

- make sure the numbers BEFORE the letters are a valid duration. Flipper can only handle 1, 2, 4, 8, 16, or 32. If there's no number before the letter, put the duration number there.
- throw onto your flipper
- play


## helpful links
- [MIDI2RTTL](https://valentin.dasdeck.com/midi/mid2rttl.php)
- [RTTL format specifications](https://www.smssolutions.net/tutorials/smart/rtttl/)