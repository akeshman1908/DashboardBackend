const config = {
  development: {
    API_URL: 'http://localhost:5000', // Local Flask backend URL
  },
  production: {
    API_URL: 'https://dashboardbackend-jych.onrender.com', // Online backend URL
  },
};

export const getConfig = () => {
  // Check of je in development of productie zit
  const env = process.env.NODE_ENV || 'development';
  return config[env];
};
