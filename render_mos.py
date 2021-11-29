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
                "name": "m1a1"
            },
            {
                "title": "生码器１-音频２",
                "audio_path": "wavs/gt2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m1a2"
            },
            {
                "title": "生码器２-音频１",
                "audio_path": "wavs/wn1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m2a1"
            },
            {
                "title": "生码器２-音频２",
                "audio_path": "wavs/wn2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m2a2"
            },
            {
                "title": "生码器３-音频１",
                "audio_path": "wavs/3bddm1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m3a1"
            },
            {
                "title": "生码器３-音频２",
                "audio_path": "wavs/3bddm2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m3a2"
            },
            {
                "title": "生码器４-音频１",
                "audio_path": "wavs/7bddm1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m4a1"
            },
            {
                "title": "生码器４-音频２",
                "audio_path": "wavs/7bddm2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m4a2"
            },
            {
                "title": "生码器５-音频１",
                "audio_path": "wavs/mel1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m5a1"
            },
            {
                "title": "生码器５-音频２",
                "audio_path": "wavs/mel2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m5a2"
            },
            {
                "title": "生码器６-音频１",
                "audio_path": "wavs/glow1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m6a1"
            },
            {
                "title": "生码器６-音频２",
                "audio_path": "wavs/glow2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m6a2"
            },
            {
                "title": "生码器７-音频１",
                "audio_path": "wavs/12bddm1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m7a1"
            },
            {
                "title": "生码器７-音频２",
                "audio_path": "wavs/12bddm2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m7a2"
            },
            {
                "title": "生码器８-音频１",
                "audio_path": "wavs/hifi1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m8a1"
            },
            {
                "title": "生码器８-音频２",
                "audio_path": "wavs/hifi2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m8a2"
            },
            {
                "title": "生码器９-音频１",
                "audio_path": "wavs/diff1.wav",
                "text": "Under the new rule visitors were not allowed to pass into the interior of the prison, but were detained between the grating.",
                "name": "m9a1"
            },
            {
                "title": "生码器９-音频２",
                "audio_path": "wavs/diff2.wav",
                "text": "This Commission can recommend no procedures for the future protection of our Presidents which will guarantee security.",
                "name": "m9a2"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
