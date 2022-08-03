# NOAA Weather Data API with Daisies

## How to Call

First, we simply load the PyDaisi package:

```python
import pydaisi as pyd
```

Next, we connect to the Daisi:

```python
noaa = pyd.Daisi("erichare/NOAA Weather")
```

Now, all we have to do is call one of the endpoints, passing in the `country_code` and `postal_code`:

```python
available_vars = noaa.available_wx_data(country_code="{cc}", postal_code="{pc}")
available_vars

noaa.forecast(country_code="US", postal_code="77001", vars=["temperature", "dewpoint"])
noaa.observations(country_code="US", postal_code="77001", vars=["temperature", "dewpoint"])
```

## Running the Streamlit App

Or, we can automate everything by just [Running the Streamlit App](https://app.daisi.io/daisies/4fab8b54-4919-4728-8d62-2318dc3457ab/app)
