import streamlit as st
import pandas as pd

from noaa_sdk import NOAA

n = NOAA()

def available_wx_data(country_code, postal_code):
    '''
    Fetch the available variables from the NOAA API

    :param str country_code: The two-digit country code of the country you're interested in
    :param str postal_code: The n-digit postal code of the area you're interested in

    :return: List of available weather variables
    '''
    res = n.get_observations(postal_code, country_code)

    return sorted(list(list(res)[0].keys()))

def forecast(country_code, postal_code, vars=None, dat=None):
    '''
    Fetch the forecast for the given postal code from the NOAA API

    :param str country_code: The two-digit country code of the country you're interested in
    :param str postal_code: The n-digit postal code of the area you're interested in
    :param list vars: The list of variables to include in the output
    :param dict dat: If provided, the data pre-fetched for inclusion

    :return: Weather forecast of the given variables for the given area
    '''
    if not dat:
        dat = n.get_forecasts(postal_code, country_code, type='forecastGridData')
        
    if not vars:
        vars = []

    return {k:v for k, v in dat.items() if k in vars}

def observations(country_code, postal_code, vars=None, dat=None):
    '''
    Fetch the weather observations for the given postal code from the NOAA API

    :param str country_code: The two-digit country code of the country you're interested in
    :param str postal_code: The n-digit postal code of the area you're interested in
    :param list vars: The list of variables to include in the output
    :param dict dat: If provided, the data pre-fetched for inclusion

    :return: Weather observations of the given variables for the given area
    '''
    if not dat:
        dat = n.get_observations(postal_code, country_code)
        
    if not vars:
        vars = []

    return {k:v for k, v in list(dat)[0].items() if k in vars}


if __name__ == "__main__":
    st.title("NOAA Weather API Interface")
    st.write("This Daisi, powered by the `noaa-sdk` Python package, allows for an interaction with the NOAA API for pulling weather forecast data.")
    
    with st.sidebar:
        cc = st.text_input("Country Code", value="US")
        pc = st.text_input("Postal Code", value="77001")

        wx_keys = available_wx_data(cc, pc)

        vars = st.multiselect("Weather Metrics", options=wx_keys, default=["temperature", "dewpoint"])

    tab1, tab2 = st.tabs(["Forecast", "Observations"])

    with tab1:
        with st.spinner(f"Fetching weather forecast for {cc}, please wait..."):
            my_forc = forecast(country_code=cc, postal_code=pc, vars=vars, dat=None)

            with st.expander("Inference with PyDaisi", expanded=True):
                st.markdown(f"""
                ```python
                import pydaisi as pyd

                noaa = pyd.Daisi("erichare/NOAA Weather")
                noaa.forecast(country_code="{cc}", postal_code="{pc}", vars={str(vars)})
                ```
                """)

            st.json(my_forc)

    with tab2:
        with st.spinner(f"Fetching weather observations for {cc}: {pc}, please wait..."):
            my_obs = observations(country_code=cc, postal_code=pc, vars=vars, dat=None)

            with st.expander("Inference with PyDaisi", expanded=True):
                st.markdown(f"""
                ```python
                import pydaisi as pyd

                noaa = pyd.Daisi("erichare/NOAA Weather")
                noaa.observations(country_code="{cc}", postal_code="{pc}", vars={str(vars)})
                ```
                """)

            st.json(my_obs)

