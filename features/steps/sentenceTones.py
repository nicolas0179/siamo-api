from behave import when, then
from hamcrest import assert_that, equal_to

from app.application.tone_identifier_service import ToneIdentifierService
from app.infrastructure.services.tokenizer_service import TokenizerService
from app.schema.tone_identifier_response import ToneIdentifierResponse

tokenizer_service = TokenizerService()
tone_identifier_service = ToneIdentifierService(tokenizer_service)


@when("I look up the lexical tone of each syllable of the sentence {sentence}")
def lookupSentenceLexicalTones(context, sentence):
    sentenceTones: ToneIdentifierResponse = (
        tone_identifier_service.process_sentence(sentence)
    )
    context.tones = [s.tone.name for s in sentenceTones.syllables]
    context.segmentation = [s.syllable for s in sentenceTones.syllables]
    context.romanization = [s.romanization for s in sentenceTones.syllables]


@then(
    "I should expect the segmentation {segmentation} with the romanization {romanization} and the tones {tones}"
)
def thenShouldExpectSegmentationAndTones(
    context, segmentation, romanization, tones
):
    expected_segmentation = segmentation.split(",")
    expected_romanization = romanization.split(",")
    expected_tones = tones.split(",")
    actual_segmentation = context.segmentation
    actual_romanization = context.romanization
    actual_tones = context.tones
    assert_that(actual_segmentation, equal_to(expected_segmentation))
    assert_that(actual_romanization, equal_to(expected_romanization))
    assert_that(actual_tones, equal_to(expected_tones))
