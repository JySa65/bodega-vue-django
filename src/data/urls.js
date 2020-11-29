export const API_BASE_URL = 'http://127.0.0.1:8000/'
export const API_V1 = `${API_BASE_URL}api/v1/`

export const getProducts = (filters) => `${API_V1}product/?${filters}`

export const getCategories = `${API_V1}product/category`

export const getPriceUSD = `${API_V1}generic/price-usd`
