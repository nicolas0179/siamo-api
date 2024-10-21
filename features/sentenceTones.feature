Feature: Tone determination of a sentence

  Scenario Outline: Determine the lexical tone of each syllable of a sentence
    When I look up the lexical tone of each syllable of the sentence <sentence>
    Then I should expect the segmentation <segmentation> with the romanization <romanization> and the tones <tones>
    Examples:
      | sentence                 | segmentation                   | romanization                 | tones                                                                    |
      | ประเทศไทย                | ประ,เทศ,ไทย                    | pra,thet,thai                | LOW_TONE,FALLING_TONE,MID_TONE                                           |
      | เก็บวันนี้พรุ่งนี้ก็เก่ง | เก็บ,วัน,นี้,พรุ่ง,นี้,ก็,เก่ง | kep,wan,ni,phrung,ni,ko,keng | LOW_TONE,MID_TONE,HIGH_TONE,FALLING_TONE,HIGH_TONE,FALLING_TONE,LOW_TONE |