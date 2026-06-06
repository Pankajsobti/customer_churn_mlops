const form =
document.getElementById(
    "predictionForm"
);

form.addEventListener(
    "submit",
    async (e) => {

        e.preventDefault();

        const data = {

            gender: "Female",

            SeniorCitizen: 0,

            Partner: "Yes",

            Dependents: "No",

            tenure: Number(
                document.getElementById(
                    "tenure"
                ).value
            ),

            PhoneService: "Yes",

            MultipleLines: "No",

            InternetService: "DSL",

            OnlineSecurity: "No",

            OnlineBackup: "Yes",

            DeviceProtection: "No",

            TechSupport: "No",

            StreamingTV: "No",

            StreamingMovies: "No",

            Contract:
            document.getElementById(
                "contract"
            ).value,

            PaperlessBilling: "Yes",

            PaymentMethod:
            "Electronic check",

            MonthlyCharges:
            Number(
                document.getElementById(
                    "monthlyCharges"
                ).value
            ),

            TotalCharges:
            Number(
                document.getElementById(
                    "totalCharges"
                ).value
            )
        };

        const response =
        await fetch(
            "http://127.0.0.1:8000/predict",
            {

                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body:
                JSON.stringify(data)
            }
        );

        const result =
        await response.json();

        document.getElementById(
            "result"
        ).innerHTML =
        result.prediction;
    }
);