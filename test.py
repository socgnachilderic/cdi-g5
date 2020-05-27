from app import generate_members


def test_generate_members():
    assert generate_members() == [
        " SIAKAM Omer", "SOCGNA Childéric",
        "TAOUSSET Abdoul", "TCHEUPI Jonathan",
        "TCHUEM Dimitri", "TCHUEM Nelson", "Wamba Gabin"
    ]
