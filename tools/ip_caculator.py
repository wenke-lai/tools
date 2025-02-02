import ipaddress


def calculate_subnets(cidr: str, subnet_mask: int) -> dict:
    """
    Calculate subnet information for a given CIDR and desired subnet mask.

    Args:
        cidr (str): Original CIDR notation (e.g., '10.0.0.0/16')
        subnet_mask (int): Desired subnet mask (e.g., 24)

    Returns:
        dict: Dictionary containing subnet information including:
            - total_subnets: Number of possible subnets
            - hosts_per_subnet: Number of usable hosts per subnet
            - subnet_cidrs: List of all subnet CIDRs
    """
    try:
        network = ipaddress.ip_network(cidr)
        original_mask = network.prefixlen

        # Validate subnet mask
        if subnet_mask <= original_mask:
            raise ValueError("Subnet mask must be larger than original CIDR mask")
        if subnet_mask > 32:
            raise ValueError("Subnet mask cannot be larger than 32")

        total_subnets = 2 ** (subnet_mask - original_mask)

        # subtract 2 for network and broadcast addresses
        hosts_per_subnet = 2 ** (32 - subnet_mask) - 2

        # Generate list of subnet CIDRs
        subnet_cidrs = [
            str(subnet) for subnet in network.subnets(new_prefix=subnet_mask)
        ]

        return {
            "total_subnets": total_subnets,
            "hosts_per_subnet": hosts_per_subnet,
            "subnet_cidrs": subnet_cidrs,
        }

    except ValueError as e:
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Example 1: Calculate subnets for 10.0.0.0/16 with /24 mask
    result1 = calculate_subnets("10.0.0.0/16", 24)
    print("Example 1 - 10.0.0.0/16 to /24:")
    print(f"Total subnets: {result1['total_subnets']}")
    print(f"Hosts per subnet: {result1['hosts_per_subnet']}")
    print(f"subnets: {result1['subnet_cidrs'][:3]}, etc.")
    print()

    # Example 2: Calculate subnets for 192.168.0.0/24 with /26 mask
    result2 = calculate_subnets("192.168.0.0/24", 26)
    print("Example 2 - 192.168.0.0/24 to /26:")
    print(f"Total subnets: {result2['total_subnets']}")
    print(f"Hosts per subnet: {result2['hosts_per_subnet']}")
    print(f"subnets: {result2['subnet_cidrs']}")
