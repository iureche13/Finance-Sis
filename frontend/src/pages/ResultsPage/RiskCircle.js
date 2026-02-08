import React from "react";

function RiskCircle({ score }) {
  // Determine the color based on the score
  let color;
  if (score > 60) color = "red";
  else if (score > 30) color = "yellow";
  else color = "green";

  const radius = 50; // circle radius
  const stroke = 10; // thickness
  const normalizedRadius = radius - stroke / 2;
  const circumference = normalizedRadius * 2 * Math.PI;
  const strokeDashoffset =
    circumference - (score / 100) * circumference; // fill percent

  return (
    <svg height={radius * 2} width={radius * 2}>
      <circle
        stroke="#e6e6e6"
        fill="transparent"
        strokeWidth={stroke}
        r={normalizedRadius}
        cx={radius}
        cy={radius}
      />
      <circle
        stroke={color}
        fill="transparent"
        strokeWidth={stroke}
        strokeDasharray={circumference + " " + circumference}
        style={{ strokeDashoffset, transition: "stroke-dashoffset 1s ease" }}
        strokeLinecap="round"
        r={normalizedRadius}
        cx={radius}
        cy={radius}
      />
      <text
        x="50%"
        y="50%"
        textAnchor="middle"
        dy="0.3em"
        fontSize="18"
        fontWeight="bold"
        fill="#333"
      >
        {score}%
      </text>
      <text
        x="50%"
        y="70%"
        textAnchor="middle"
        fontSize="12"
        fill="#555"
      >
        Risk Score
      </text>
    </svg>
  );
}

export default RiskCircle;
