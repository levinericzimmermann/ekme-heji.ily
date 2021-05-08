"""Script for building HEJI Ekmelily tuning files."""

if __name__ == "__main__":
    from mutwo.converters.frontends import ekmelily
    from mutwo.parameters import pitches_constants

    for reference in pitches_constants.ASCENDING_DIATONIC_PITCH_NAMES:
        converter = ekmelily.HEJIEkmelilyTuningFileConverter(
            path="ekme-heji/ekme-heji-ref-{}.ily".format(reference),
            reference_pitch=reference,
        )
        converter.convert()
