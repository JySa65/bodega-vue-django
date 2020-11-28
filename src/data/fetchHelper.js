const fetchHelper = (url, options = {}, { useToken = true, multipart = false } = {}) => {
  const fetchOptions = {
    method: 'GET',
    headers: {
      Accept: 'application/json'
    },
    ...options
  }

  if (fetchOptions.method !== 'GET' && fetchOptions.body && !multipart) {
    fetchOptions.headers['Content-Type'] = 'application/json'
    fetchOptions.body = JSON.stringify(fetchOptions.body)
  }

  return fetch(url, fetchOptions).then((response) => {
    if (response.status === 401 && useToken) {
      console.log(response)
      return Promise.resolve({})
    }

    if (response.status >= 400 && response.status !== 401 && response.status < 500) {
      return response.json().then((message) => {
        const error = {
          message: `Bad response from server at ${response.url} => ${response.status}, ${response.statusText}`,
          url: response.url,
          status: +response.status,
          statusText: response.statusText,
          data: message
        }
        const { msg, msgs } = message
        error.message = msg || msgs || message
        const nonFieldErrors = message.non_field_errors || error.message.non_field_errors

        if (nonFieldErrors !== undefined) {
          const text = nonFieldErrors[0]
          error.message = text
        }

        return Promise.reject(error)
      })
    }
    if (response.status === 500) {
      const error = {
        message: 'Hubo un problema al procesar tu petición. Por favor intenta nuevamente más tarde.',
        url: response.url,
        status: +response.status,
        statusText: response.statusText,
        data: response.data
      }

      return Promise.reject(error)
    }
    return response.json().then((data) =>
      Promise.resolve({
        status: response.status,
        data
      })
    )
  })
}

export default fetchHelper
