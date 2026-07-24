import os
import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Fallback for local development
if not SUPABASE_URL:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]

if not SUPABASE_KEY:
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)