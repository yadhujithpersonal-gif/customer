const API =
    "http://127.0.0.1:8000";


async function loadDashboard() {

    const response =
        await fetch(
            `${API}/dashboard`
        );

    const data =
        await response.json();


    document.getElementById(
        "total"
    ).textContent =
        data.total_disputes;


    document.getElementById(
        "resolved"
    ).textContent =
        data.resolved;


    document.getElementById(
        "escalated"
    ).textContent =
        data.escalated;


    document.getElementById(
        "automation"
    ).textContent =
        data.automation_rate + "%";
}


async function loadDisputes() {

    const response =
        await fetch(
            `${API}/disputes`
        );

    const data =
        await response.json();


    const table =
        document.getElementById(
            "table"
        );


    table.innerHTML = "";


    data.forEach(d => {

        const row =
            document.createElement(
                "tr"
            );


        row.innerHTML = `

            <td>${d.id}</td>

            <td>${d.category}</td>

            <td>${d.intent}</td>

            <td>${d.status}</td>

            <td>${d.decision}</td>

        `;


        table.appendChild(row);

    });
}


async function submitDispute() {

    const customer =
        document.getElementById(
            "customer"
        ).value;


    const order =
        document.getElementById(
            "order"
        ).value;


    const message =
        document.getElementById(
            "message"
        ).value;


    if (!message.trim()) {

        alert(
            "Please enter a complaint."
        );

        return;
    }


    const response =
        await fetch(
            `${API}/disputes`,
            {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    customer_id:
                        customer,

                    order_id:
                        order,

                    message:
                        message

                })
            }
        );


    const data =
        await response.json();


    if (!response.ok) {

        alert(
            data.detail
        );

        return;
    }


    showResult(data);

    loadDashboard();

    loadDisputes();
}


function showResult(data) {

    const result =
        document.getElementById(
            "result"
        );


    const reasons =
        data.decision.reasons
            .map(
                r => `<p>✓ ${r}</p>`
            )
            .join("");


    result.innerHTML = `

        <h2>AI Analysis</h2>

        <p>
            <b>Category:</b>
            ${data.ai_analysis.category}
        </p>

        <p>
            <b>Intent:</b>
            ${data.ai_analysis.intent}
        </p>

        <p>
            <b>Sentiment:</b>
            ${data.ai_analysis.sentiment}
        </p>

        <p>
            <b>Urgency:</b>
            ${data.ai_analysis.urgency}
        </p>

        <p>
            <b>Confidence:</b>
            ${(data.ai_analysis.confidence * 100)
                .toFixed(0)}%
        </p>


        <h2>Decision</h2>

        <h3>
            ${data.decision.action}
        </h3>


        <h3>Why?</h3>

        ${reasons}


        <h2>Resolution</h2>

        <p>
            ${data.dispute.resolution}
        </p>


        <h3>
            Status:
            ${data.dispute.status}
        </h3>
    `;
}


loadDashboard();

loadDisputes();