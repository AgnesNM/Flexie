import collections
import pandas as pd
from .models import FlexieUsers
from .utils import *
import random

BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def calculate(data):

    """
    Calculates a set of values from the numeric list
    input data showing how closely the first digits
    fit the Benford Distribution.
    Results are returned as a list of dictionaries.
    """
    
    results = []
    
    if not data:
        benford_data = []

        for first_digit in range(1, 10):
            random_factor = random.uniform(0.8, 1.2)
            for num_count in range(1, int(1000 * BENFORD_PERCENTAGES[first_digit] * random_factor)):
                start = first_digit * 1000
                benford_data.append(random.randint(start, start + 1000))

        data = benford_data

    first_digits = list(map(lambda n: str(n)[0], data))
    first_digit_frequencies = collections.Counter(first_digits)

    for n in range(1, 10):

        data_frequency = first_digit_frequencies[str(n)]
        data_frequency_percent = data_frequency / len(data)
        benford_frequency = len(data) * BENFORD_PERCENTAGES[n]
        benford_frequency_percent = BENFORD_PERCENTAGES[n]
        difference_frequency = data_frequency - benford_frequency
        difference_frequency_percent = data_frequency_percent - benford_frequency_percent

        results.append({"n": n,
                        "data_frequency":               data_frequency,
                        "data_frequency_percent":       data_frequency_percent,
                        "benford_frequency":            benford_frequency,
                        "benford_frequency_percent":    benford_frequency_percent,
                        "difference_frequency":         difference_frequency,
                        "difference_frequency_percent": difference_frequency_percent})

    return results


def get_data(userObject):
    user_info = userObject.objects.last()
    data = user_info.file
    
    # get all the data from the csv file and extract a list of numbers
    df = pd.read_csv(data)
    numerical_data = df.select_dtypes(include=['number']).values.flatten().tolist()
    return numerical_data


def generate_table_html(benford_table):
    table_html = """
    <table>
        <tr>
            <th>n</th>
            <th>Data Freq</th>
            <th>Data Pct</th>
            <th>Benford Freq</th>
            <th>Benford Pct</th>
            <th>Difference Freq</th>
            <th>Difference Pct</th>
        </tr>
    """

    for item in benford_table:
        table_html += f"""
        <tr>
            <td>{item["n"]}</td>
            <td>{item["data_frequency"]}</td>
            <td>{item["data_frequency_percent"] * 100:.2f}%</td>
            <td>{item["benford_frequency"]}</td>
            <td>{item["benford_frequency_percent"] * 100:.2f}%</td>
            <td>{item["difference_frequency"]}</td>
            <td>{item["difference_frequency_percent"] * 100:.2f}%</td>
        </tr>
        """

    table_html += "</table>"
    return table_html


def generate_graph_html(benford_table):
    graph_html = """
    <div id="benford-graph">
        <h2>Benford Graph</h2>
        <div class="bar-chart">
    """

    for item in benford_table:
        data_pct = item["data_frequency_percent"] * 100
        benford_pct = item["benford_frequency_percent"] * 100
        bar_width = int(data_pct * 2)  # Adjust the multiplier for the bar width as needed

        graph_html += f"""
            <div class="bar">
                <div class="data-bar" style="width: {bar_width}px;"></div>
                <div class="label">{item["n"]}</div>
                <div class="label">{data_pct:.2f}%</div>
                <div class="label">{benford_pct:.2f}%</div>
            </div>
        """

    graph_html += """
        </div>
        <div class="legend">
            <div>Data</div>s
            <div>Benford</div>
        </div>
    </div>
    """

    return graph_html
