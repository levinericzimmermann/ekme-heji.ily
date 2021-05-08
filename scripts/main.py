"""Script for building HEJI Ekmelily tuning files."""

if __name__ == "__main__":
    from mutwo.converters.frontends import ekmelily

    converter = ekmelily.HEJIEkmelilyTuningFileConverter(
        path="ekme-heji/ekme-heji.ily",
        reference_pitch='c',
    )
    converter.convert()
