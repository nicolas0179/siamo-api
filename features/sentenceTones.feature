Feature: Tone determination of a sentence

  Scenario Outline: Determine the lexical tone of each syllable of a sentence
    When I look up the lexical tone of each syllable of the sentence <sentence>
    Then I should expect the segmentation <segmentation> with the tones <tones>
    Examples:
      | sentence                 | segmentation                   | tones                                                                    |
      | ประเทศไทย                | ประ,เทศ,ไทย                    | LOW_TONE,FALLING_TONE,MID_TONE                                           |
      | เก็บวันน้ีพรุ่งน้ีก็เก่ง | เก็บ,วัน,น้ี,พรุ่ง,น้ี,ก็,เก่ง | LOW_TONE,MID_TONE,HIGH_TONE,FALLING_TONE,HIGH_TONE,FALLING_TONE,LOW_TONE |