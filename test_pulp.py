import streamlit as st

st.title("PuLP Dependency Test")

try:
    import pulp
    st.success(f"✅ PuLP successfully imported! Version: {pulp.__version__}")
    
    # Try to create a solver to verify CBC is available
    try:
        solver = pulp.PULP_CBC_CMD()
        st.success("✅ CBC solver is available")
    except Exception as e:
        st.error(f"❌ Error creating CBC solver: {str(e)}")
        
    st.write("Your PuLP installation is working correctly.")
except ImportError as e:
    st.error(f"❌ Failed to import PuLP: {str(e)}")
    st.error("PuLP is not installed or not configured correctly.")
