# Templateify Anything

An universal template generator

This isn't anything unique, but it functions and it uses regex. Both positives, ofcourse.

Popular libraries like cookiecutter, etc. are used to substitute some stuff around in mostly python libraries. This is a generic substituter that can apply to anything.

Automate your tasks: The config/ directory is intended to be abstracted one layer further as to simplify the whole process, but it works otherwise.

What this does that makes it stand out a liiiittle more is that it substitutes text in the file directly (so dynamic variables), you can change the regex pattern if it conflicts.

Works with any file type thats readable.. otherwise - BLACKLISTED_PATHS in settings.py is a thing. See example for `.png`.

My personal use-case comes from Minecraft modding, generally you have your own template with your own dependencies and it is a *hassle* replacing the `mod_id` every single damn time. Though, definitely gonna use this for other projects.

## How it works
1. Checks path - Can substitute? Great.
2. Iterates each line, substitutes if it finds a pattern match.
3. Push to OUTPUT_DIRECTORY~
4. Get errors after realizing you forgot to blacklist a file type that can't be read-
5. F

## Credits
staying up late at night
