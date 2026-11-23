{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNwT6XKNcuxreyGtDS/ts9X",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Trendtek254/plp-da-a4-student-eda-and-board-report/blob/main/generate_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "WdIIljaViUzP"
      },
      "outputs": [],
      "source": [
        "#PYTHON · DATASET GENERATOR\n",
        "#Generator 1: STUDENT PERFORMANCE\n",
        "\n",
        "import numpy as np, pandas as pd\n",
        "\n",
        "rng = np.random.default_rng(55)\n",
        "\n",
        "n = 1200\n",
        "\n",
        "students = pd.DataFrame({\n",
        "\n",
        "    \"student_id\": range(1, n + 1),\n",
        "\n",
        "    \"county\": rng.choice([\"Nairobi\", \"Kisumu\", \"Nakuru\",\n",
        "\n",
        "                          \"Mombasa\", \"Nyeri\", \"Turkana\"], n),\n",
        "\n",
        "    \"school_type\": rng.choice([\"Public\", \"Private\"], n, p=[0.75, 0.25]),\n",
        "\n",
        "    \"gender\": rng.choice([\"F\", \"M\"], n),\n",
        "\n",
        "    \"attendance_rate\": rng.beta(8, 2, n).round(2),\n",
        "\n",
        "    \"study_hours\": rng.gamma(2.5, 2.0, n).round(1),\n",
        "\n",
        "})\n",
        "\n",
        "base = (35 + 30 * students[\"attendance_rate\"] + 2.2 * students[\"study_hours\"]\n",
        "\n",
        "        + np.where(students[\"school_type\"] == \"Private\", 6, 0))\n",
        "\n",
        "students[\"math\"] = (base + rng.normal(0, 8, n)).clip(0, 100).round(0)\n",
        "\n",
        "students[\"english\"] = (base + rng.normal(3, 7, n)).clip(0, 100).round(0)\n",
        "\n",
        "students[\"science\"] = (base + rng.normal(-2, 9, n)).clip(0, 100).round(0)\n",
        "\n",
        "students.to_csv(\"student_performance.csv\", index=False)\n",
        "\n",
        "#Generator 2: DUKA ELECTRONICS\n",
        "\n",
        "rng = np.random.default_rng(2026)\n",
        "\n",
        "n = 1000\n",
        "\n",
        "products = {\n",
        "    \"Phone\": 15000,\n",
        "    \"Laptop\": 65000,\n",
        "    \"Headphones\": 2500,\n",
        "    \"Tablet\": 28000,\n",
        "    \"Charger\": 1200\n",
        "}\n",
        "\n",
        "sales = pd.DataFrame({\n",
        "\n",
        "    \"order_id\": range(1001, 1001 + n),\n",
        "\n",
        "    \"order_date\": pd.to_datetime(\"2026-01-01\")\n",
        "                  + pd.to_timedelta(rng.integers(0, 180, n), unit=\"D\"),\n",
        "\n",
        "    \"branch\": rng.choice([\"Nairobi\", \"Mombasa\", \"Kisumu\",\n",
        "                          \"Nakuru\", \"Eldoret\"], n,\n",
        "                         p=[0.4, 0.2, 0.15, 0.15, 0.1]),\n",
        "\n",
        "    \"product\": rng.choice(list(products), n),\n",
        "\n",
        "    \"quantity\": rng.integers(1, 6, n),\n",
        "\n",
        "    \"channel\": rng.choice([\"In-store\", \"Online\", \"Phone order\"], n,\n",
        "                          p=[0.55, 0.35, 0.10]),\n",
        "\n",
        "})\n",
        "\n",
        "sales[\"unit_price\"] = sales[\"product\"].map(products)\n",
        "\n",
        "sales.to_csv(\"duka_sales.csv\", index=False)\n",
        "\n",
        "\n"
      ]
    }
  ]
}