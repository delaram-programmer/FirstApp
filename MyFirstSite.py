import streamlit as st

st.text("""
I know every child wants to say certain things
to their mom to tell her how much they love her, but for
some reason, it often doesn’t happen! So send this to her
so she knows how much you love her.
""")

st.title("A letter for my MOM")

long_text = ("""
“My beautiful mom, I want to tell you things that I’ve never
said before. I want you to know that there is no one superior
to you in this world. Know that you are the most valuable
and beloved part of my life. I’m willing to do anything for
you; just say the word, and I would give my life for you.
I would die and be reborn a thousand times just to see
your smiles. You are my world, and know that if you’re 
not here, neither am I. Life, even for a moment without
you, would be hell for me. So please stay with me until
the end of my life. I promise to push aside anyone who 
stands in your way, and even if the whole world is
against you, I’m behind you and will always stand by
you.”
""")
st.code(long_text, language='text')

st.error("I love you, my everything.")