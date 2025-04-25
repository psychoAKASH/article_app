module.exports = {
    content: [
        "./templates/**/*.html",
         "./static/**/*.css"
         ],
    theme: {
        extend: {},
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
}