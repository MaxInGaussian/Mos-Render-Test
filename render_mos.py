#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS 實驗表單 1",
        form_url="https://script.google.com/macros/s/AKfycbzlwvyfbZQJQ6yfjrRjaPoBArriqW4Z-ydgMxBto-zgP7erZBquuJtetl3KEkuI0ueG/exec",
        form_id=1,
        questions=[
            {
                "title": "生码器１-音频１",
                "audio_path": "wavs/gt1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q1"
            },
            {
                "title": "生码器１-音频２",
                "audio_path": "wavs/gt2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q2"
            },
            {
                "title": "生码器２-音频１",
                "audio_path": "wavs/wn1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q3"
            },
            {
                "title": "生码器２-音频２",
                "audio_path": "wavs/wn2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q4"
            },
            {
                "title": "生码器３-音频１",
                "audio_path": "wavs/3bddm1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q5"
            },
            {
                "title": "生码器３-音频２",
                "audio_path": "wavs/3bddm2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q6"
            },
            {
                "title": "生码器４-音频１",
                "audio_path": "wavs/7bddm1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q7"
            },
            {
                "title": "生码器４-音频２",
                "audio_path": "wavs/7bddm2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q8"
            },
            {
                "title": "生码器５-音频１",
                "audio_path": "wavs/mel1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q9"
            },
            {
                "title": "生码器５-音频２",
                "audio_path": "wavs/mel2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q10"
            },
            {
                "title": "生码器６-音频１",
                "audio_path": "wavs/glow1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q11"
            },
            {
                "title": "生码器６-音频２",
                "audio_path": "wavs/glow2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q12"
            },
            {
                "title": "生码器７-音频１",
                "audio_path": "wavs/12bddm1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q13"
            },
            {
                "title": "生码器７-音频２",
                "audio_path": "wavs/12bddm2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q14"
            },
            {
                "title": "生码器８-音频１",
                "audio_path": "wavs/hifi1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q15"
            },
            {
                "title": "生码器８-音频２",
                "audio_path": "wavs/hifi2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q16"
            },
            {
                "title": "生码器９-音频１",
                "audio_path": "wavs/diff1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "q17"
            },
            {
                "title": "生码器９-音频２",
                "audio_path": "wavs/diff2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "q18"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
