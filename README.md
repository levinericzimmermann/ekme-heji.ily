# ekme-heji.ily - Helmholtz-Ellis JI Notation for Lilypond

This package adds support for the [Extended Helmholtz-Ellis JI Pitch Notation](https://marsbat.space/pdfs/notation.pdf)
in Lilypond > 2.19 via [Ekmelily](http://www.ekmelic-music.org/en/extra/ekmelily.htm) and the
[Ekmelos font](http://www.ekmelic-music.org/en/extra/ekmelos.htm) from Thomas Richter.

## Installation

First follow the installation instructions for [Ekmelily](http://www.ekmelic-music.org/en/extra/ekmelily.htm#Installation)
and [Ekmelos](http://www.ekmelic-music.org/en/extra/ekmelos.htm#Installation). Then download
the recent _ekme-heji.ily_ package and include the respective _ekme-heji.ily_ file in your
Lilypond project:

## Usage and nomenclature

_ekme-heji.ily_ adds new pitches to Lilypond. The pitches follow a logical nomenclature to differentiate between intonations.
The name of a _ekme-heji.ily_ pitch is composed of:

1. diatonic pitch name
2. (optional) Pythagorean accidental ('s' for sharp, 'ss' for double sharp, 'f' for flat, 'ff' for double flat)
3. (optional) additional commas

Commas are described by three letters, where

1. the first letter indicates the tonality: `o` for otonality (exponents bigger than 0) and `u` for utonality (exponents smaller than 0)
2. the second letter indicates the prime number: `a` for 5, `b` for 7, `c` for 11, ...
3. the last letter indicates the exponent: `a` for 1, `b` for 2, `c` for 3

Therefore a 5/4 pitch to c would be denoted with eoaa (diatonic pitch name: e, comma: `oaa` for otonality of 5 with exponent 1).
When a pitch owns several commas they are always sorted from lower prime numbers to higher prime numbers. For instance the diatonic pitch 'a' with two syntonic commas and one undecimal commas would be written as `aoaboca`.

Tempered pitches are indicated by the letter `t`. For instance a tempered `d` would be `dt` and a tempered f-sharp would be `fst`.

## Example

Writing a [Wilson Hexany](http://anaphoria.com/wilsoncps.html) in HEJI - Notation:

```lilypond
\version "2.22.0"
\language "english"

\include "ekme-heji-ref-a.ily"

\new Score
<<
    \new Staff
    {
        \new Voice
        {
            \accidentalStyle "dodecaphonic"
            aoca'1
            boaaoba'
            cobaoca''
            doba''1
            fsoaaoca''1
            gsoaa''1
        }
    }
>>
```

![wilson](examples/wilson_hexany.png)

## Precision

The midi rendering is precise up to +/- 0.2 cents.

## Limitations

By default not all specified accidentals and accidental combinations are supported. The highest implemented prime number is 17 although the [Helmholtz-Ellis JI Pitch Notation](https://marsbat.space/pdfs/notation.pdf) defines accidentals until 47.
There are two reasons for this limitation:

1. Lilypond takes too long to parse if all specified accidental combinations are added.
2. The [Ekmelos font](http://www.ekmelic-music.org/en/extra/ekmelos.htm) only supports accidentals until prime number 31. This could be solved in future releases of Ekmelos or through using a different font.

For now, _ekme-heji.ily_ is only available in English (English diatonic pitch names, English default accidentals like 's' for sharp and 'f' for flat).

## Modifications

If you want to build your own tuning files with different nomenclature or different supported prime numbers, you can adjust the Python script which builds the tuning files.
