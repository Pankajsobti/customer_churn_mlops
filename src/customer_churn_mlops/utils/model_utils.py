from sklearn.metrics import roc_auc_score


def evaluate_models(X_train, y_train, X_test, y_test, models):

    report = {}

    for model_name, model in models.items():

        model.fit(X_train, y_train)

        y_pred_proba = model.predict_proba(X_test)[:, 1]

        score = roc_auc_score(
            y_test,
            y_pred_proba
        )

        report[model_name] = score

    return report