"""Script for building HEJI Ekmelily tuning files."""

if __name__ == "__main__":
    from mutwo import ekmelily_converters

    for set_microtonal_tuning, suffix in ((True, ""), (False, "-no-microtones")):
        c = ekmelily_converters.HEJIEkmelilyTuningFileConverter(
            path=f"ekme-heji/ekme-heji{suffix}.ily",
            reference_pitch="c",
            set_microtonal_tuning=set_microtonal_tuning,
        )
        c.convert()
