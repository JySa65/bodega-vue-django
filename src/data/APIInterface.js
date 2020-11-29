import _fetch from './fetchHelper'
import * as urls from './urls'

export const getProducts = (filters = '') => _fetch(urls.getProducts(filters))

export const getCategories = () => _fetch(urls.getCategories)

export const getPriceUSD = () => _fetch(urls.getPriceUSD)
